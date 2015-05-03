from .gridcurves import GridCurves

class ConformalMap(object):
    def __init__(self, domain = None, range = None, *args):
        self._domain = domain
        self._range  = range

    @property
    def range(self):
        return self._range

    @property
    def domain(self):
        return self._domain

    def __call__(self, z):
        return self.apply(z)

    def apply(self, z):
        if isinstance(z, GridCurves):
            return GridCurves([ self.applyMap(c) for c in z.curves ])
        else:
            return self.applyMap(z)

    def applyMap(self, z):
        return z

    def __str__(self):
        return '**conformalmap object**\n\n'

    #function disp(f)
        #fprintf('** conformalmap object **\n\n')
        #if ~isempty(f.theDomain)
            #fprintf('---\nhas domain\n')
            #disp(f.theDomain)
        #end
        #if ~isempty(f.theRange)
            #fprintf('---\nhas range\n')
            #disp(f.theRange)
        #end

        #if iscomposition(f)
            #fprintf('---\nthis map is a composition of:\n(in order of application)\n')
            #for k = 1:numel(f.functionList)
                #disp(f.functionList{k})
            #end
        #end
    #end

    def plot(self, *args, **kwargs):
        self(self.domain).plot()

    #function out = plot(f, varargin)
        #washold = ishold;

        #if isempty(f.theRange) || ...
                #~(isempty(f.theDomain) || hasgrid(f.theDomain))
            #warning('Map range not set or domain has an empty grid. No plot produced.')
            #return
        #end

        #cah = newplot;
        #hold on
        
        #% Separate grid construction and plot 'name'/value pairs.
        #[gargs, pargs] = separateArgs(get(f.theDomain), varargin{:}); 
        #hg = plot(apply(f, grid(f.theDomain, gargs{:})), pargs{:});
        #hb = plot(f.theRange, pargs{:});

        #if ~washold
            #cmtplot.whitefigure(get(cah, 'parent'))
            #axis(plotbox(f.theRange))
            #aspectequal
            #if cmtplot.hasNewGraphics
                #% Bug in new graphics won't show smoothed lines if this
                #% isn't done when drawing on a figure created by the plot
                #% call. Just need some way to force a redraw after
                #% the lines are put up.
                #drawnow
            #end
            #axis off
            #hold off
        #end

        #if nargout
            #out = [hg; hb];
        #end
    #end


#methods
#% Arithmetic operators.
    #function f = mtimes(f1, f2)
        #% Interpret f1*f2 as the composition f1(f2(z)), or as scalar times
        #% the image.

        #% Make sure a conformalmap is first.
        #if isnumeric(f1)
            #tmp = f1;  f1 = f2;  f2 = tmp;
        #end

        #if isnumeric(f2)
            #const = f2;  % for naming
            #f = conformalmap(f1,@(z) const*z);
        #elseif isa(f2,'conformalmap')
            #% Do a composition of the two maps.
            #f = conformalmap(f2, f1);
        #else
            #error('CMT:conformalmap:mtimes',...
                #'Must either multiply by a scalar or compose two maps.')
        #end
    #end

    #function g = minus(f,c)
        #if isnumeric(f)
            #g = plus(-f,c);
        #else
            #g = plus(f,-c);
        #end
    #end

    #function g = plus(f,c)
        #% Defines adding a constant (translation of the range).

        #if isnumeric(f)
            #tmp = c;  c = f;  f = tmp;
        #end

        #if ~isnumeric(c) || (length(c) > 1)
            #error('CMT:conformalmap:plus',...
                #'You may only add a scalar to a conformalmap.')
        #end

        #g = conformalmap( f, @(z) z+c );
    #end

    #function g = mpower(f,n)

        #if (n ~= round(n)) || (n < 0)
            #error('CMT:conformalmap:integerpower',...
                #'Power must be a positive integer.')
        #end

        #g = f;
        #p = floor(log2(n));
        #for k = 1:p
            #g = conformalmap(g,g);
        #end
        #for k = n-p
            #g = conformalmap(g,f);
        #end
    #end

    #function g = uminus(f)
        #g = conformalmap( f, @(z) -z );
    #end
#end


