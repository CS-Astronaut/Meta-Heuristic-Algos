# benchfunc.py - auto-generated (partial/full) from uploaded spreadsheet
# Implementations vectorized with numpy (input X shaped (..., dim))
import numpy as np

def _ensure_ndarray(X):
    X = np.asarray(X)
    return X


# Implementations

def ackley(X):
    X = _ensure_ndarray(X)
    n = X.shape[-1]
    sum_sq = np.sum(X**2, axis=-1)
    cos_term = np.sum(np.cos(2.0*np.pi*X), axis=-1)
    return -20.0*np.exp(-0.2*np.sqrt(sum_sq/n)) - np.exp(cos_term/n) + 20.0 + np.e


def ackleyn2(X):
    return ackley(X)


def ackleyn3(X):
    return ackley(X)


def ackleyn4(X):
    return ackley(X)


def adjiman(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return np.cos(x) * np.cos(y) + np.sin(x) + np.cos(y) + (x*y)


def alpinen1(X):
    X = _ensure_ndarray(X)
    return np.sum(np.abs(X * np.sin(X) + 0.1*X), axis=-1)


def alpinen2(X):
    X = _ensure_ndarray(X)
    return np.sum(np.sqrt(np.abs(X)) + np.sin(X), axis=-1)


def bartelsconn(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return np.abs(x**2 + y**2 + x*y) + np.abs(2*x - 3*y) + np.abs(x + y)


def beale(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2


def bird(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return np.sin(x)*np.exp((1-np.cos(y))**2) + np.cos(y)*np.exp((1-np.sin(x))**2) + (x - y)**2


def bohachevskyn1(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return x**2 + 2.0*y**2 - 0.3*np.cos(3.0*np.pi*x) - 0.4*np.cos(4.0*np.pi*y) + 0.7


def bohachevskyn2(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return x**2 + 2*y**2 - 0.3*np.cos(3*np.pi*x)*np.cos(4*np.pi*y) + 0.3


def booth(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return (x + 2*y - 7.0)**2 + (2*x + y - 5.0)**2


def brent(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return (x + 10.0)**2 + (y + 10.0)**2 + np.exp(-x**2 - y**2)


def brown(X):
    X = _ensure_ndarray(X)
    # Brown function: sum_{i=1}^{n-1} (x_i^2)^(x_{i+1}^2+1) + (x_{i+1}^2)^(x_i^2+1)
    x = X
    xi = x[..., :-1]
    xnext = x[..., 1:]
    return np.sum( (xi**2)**(xnext**2+1.0) + (xnext**2)**(xi**2+1.0), axis=-1 )


def bukinn6(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return 100.0*np.sqrt(np.abs(y - 0.01*x**2)) + 0.01*np.abs(x + 10.0)



def carromtable(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    s = 1.0 - (np.sqrt(x**2 + y**2) / np.pi)
    return - (1.0/30.0) * np.exp(2.0 * np.abs(s)) * (np.cos(x)**2) * (np.cos(y)**2)




def crossintray(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    a = np.abs(np.sin(x) * np.sin(y) * np.exp(np.abs(100.0 - np.sqrt(x**2 + y**2)/np.pi)))
    return -0.0001 * (a + 1.0)**0.1




def deckkersaarts(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    r2 = x**2 + y**2
    return 105.0*x**2 + y**2 - r2**2 + 1e-5 * r2**4




def dropwave(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    r = np.sqrt(x**2 + y**2)
    return - (1.0 + np.cos(12.0 * r)) / (0.5 * (x**2 + y**2) + 2.0)



def easom(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return -np.cos(x)*np.cos(y)*np.exp(-((x-np.pi)**2 + (y-np.pi)**2))



def eggcrate(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return x**2 + y**2 + 25.0*(np.sin(x)**2 + np.sin(y)**2)




def elattar(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return (x**2 + y - 10.0)**2 + (x + y**2 - 7.0)**2 + (x**2 + y**3 - 1.0)**2




def exponential(X):
    X = _ensure_ndarray(X)
    return -np.exp(-0.5 * np.sum(X**2, axis=-1))




def forrester(X):
    X = _ensure_ndarray(X)
    x = X[...,0]
    return (6.0*x - 2.0)**2 * np.sin(12.0*x - 4.0)



def goldsteinprice(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    term1 = (1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2))
    term2 = (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2))
    return term1 * term2



def gramacylee(X):
    X = _ensure_ndarray(X)
    # simplified surrogate-like Gramacy-Lee test surface (approximation)
    x = X[...,0]; y = X[...,1]
    return (x - 1.0)**2 + (y - 2.0)**2 + np.sin(3*x + 1.5*y)



def griewank(X):
    X = _ensure_ndarray(X)
    i = np.arange(1, X.shape[-1]+1)
    sum_term = np.sum(X**2, axis=-1)/4000.0
    prod_term = np.prod(np.cos(X/np.sqrt(i)), axis=-1)
    return sum_term - prod_term + 1.0



def happycat(X, alpha=0.5):
    X = _ensure_ndarray(X)
    d = X.shape[-1]
    norm = np.sum(X**2, axis=-1)
    return (np.sum(X, axis=-1)**2 / d**2)**alpha + (norm - d)**2



def himmelblau(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return (x**2 + y - 11.0)**2 + (x + y**2 - 7.0)**2



def holdertable(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return -np.abs(np.sin(x) * np.cos(y) * np.exp(np.abs(1.0 - np.sqrt(x**2 + y**2)/np.pi)))




def keane(X):
    X = _ensure_ndarray(X)
    # Keane's Bump (approximation)
    return -np.prod(np.sin(X), axis=-1) / np.sum(X**2, axis=-1)




def leon(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return 100*(y - x**2)**2 + (1 - x)**2 + 90*(y - x**2)**4




def levin13(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return np.sin(8*x) + np.sin(4*y) + (x - 0.5)**2 + (y - 0.5)**2




def matyas(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return 0.26*(x**2 + y**2) - 0.48*x*y




def mccormick(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return np.sin(x + y) + (x - y)**2 - 1.5*x + 2.5*y + 1.0




def periodic(X):
    X = _ensure_ndarray(X)
    return np.sum(np.sin(X)**2, axis=-1)




def powellsum(X):
    X = _ensure_ndarray(X)
    # Powell sum (approx variant)
    i = np.arange(1, X.shape[-1]+1)
    return np.sum((i * X)**2, axis=-1)




def qing(X):
    X = _ensure_ndarray(X)
    i = np.arange(1, X.shape[-1]+1)
    return np.sum((X - i)**2, axis=-1)




def quartic(X, noise=False):
    X = _ensure_ndarray(X)
    i = np.arange(1, X.shape[-1]+1)
    base = np.sum(i * X**4, axis=-1)
    if noise:
        base = base + np.random.random(size=base.shape)
    return base



def rastrigin(X):
    X = _ensure_ndarray(X)
    n = X.shape[-1]
    return 10.0*n + np.sum(X**2 - 10.0*np.cos(2.0*np.pi*X), axis=-1)



def ridge(X):
    X = _ensure_ndarray(X)
    n = X.shape[-1]
    i = np.arange(1, n+1)
    return np.sum(i * X**2, axis=-1)



def rosenbrock(X):
    X = _ensure_ndarray(X)
    xi = X[..., :-1]
    xnext = X[..., 1:]
    return np.sum(100.0*(xnext - xi**2)**2 + (xi - 1.0)**2, axis=-1)



def salomon(X):
    X = _ensure_ndarray(X)
    norm = np.sqrt(np.sum(X**2, axis=-1))
    return 1.0 - np.cos(2.0*np.pi*norm) + 0.1 * norm




def schaffern1(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    denom = (1.0 + 0.001*(x**2 + y**2))**2
    num = np.sin(x**2 - y**2)**2 - 0.5
    return 0.5 + num / denom




def schaffern2(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    denom = (1.0 + 0.001*(x**2 + y**2))**2
    num = np.cos(np.sin(np.abs(x) - np.abs(y))) - 0.5
    return 0.5 + num / denom




def schaffern3(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    denom = (1.0 + 0.001*(x**2 + y**2))**2
    num = np.sin(np.sqrt(x**2 + y**2))**2 - 0.5
    return 0.5 + num / denom




def schaffern4(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return 0.5 + (np.cos(np.sin(np.abs(x) - np.abs(y))) - 0.5)




def schwefel220(X):
    X = _ensure_ndarray(X)
    return np.max(np.abs(X), axis=-1)




def schwefel221(X):
    X = _ensure_ndarray(X)
    return np.sum(np.abs(X), axis=-1)




def schwefel222(X):
    X = _ensure_ndarray(X)
    return np.sum(np.abs(X) + np.prod(np.abs(X), axis=-1))




def schwefel223(X):
    X = _ensure_ndarray(X)
    # variant placeholder
    return np.sum(X**2, axis=-1) - np.prod(np.cos(X), axis=-1)



def schwefel(X):
    X = _ensure_ndarray(X)
    n = X.shape[-1]
    return 418.9829 * n - np.sum(X * np.sin(np.sqrt(np.abs(X))), axis=-1)


def shubertn3(X):
    return shubert(X)


def shubertn4(X):
    return shubert(X)


def shubert(X):
    X = _ensure_ndarray(X)
    # classical 2-D Shubert (extendable)
    if X.shape[-1] == 1:
        x = X[...,0]
        s = 0.0
        for i in range(1,6):
            s += i * np.cos((i+1)*x + i)
        return s
    elif X.shape[-1] == 2:
        x = X[...,0]; y = X[...,1]
        s1 = 0.0; s2 = 0.0
        for i in range(1,6):
            s1 += i * np.cos((i+1)*x + i)
            s2 += i * np.cos((i+1)*y + i)
        return s1 * s2
    else:
        # product across dims
        prods = 1.0
        for dim in range(X.shape[-1]):
            xi = X[..., dim]
            s = 0.0
            for i in range(1,6):
                s += i * np.cos((i+1)*xi + i)
            prods = prods * s
        return prods


def sphere(X):
    X = _ensure_ndarray(X)
    return np.sum(X**2, axis=-1)


def styblinskitank(X):
    X = _ensure_ndarray(X)
    return 0.5 * np.sum(X**4 - 16.0*X**2 + 5.0*X, axis=-1)


def sumsquares(X):
    X = _ensure_ndarray(X)
    i = np.arange(1, X.shape[-1]+1)
    return np.sum(i * X**2, axis=-1)


def threehumpcamel(X):
    X = _ensure_ndarray(X)
    x = X[...,0]; y = X[...,1]
    return 2.0*x**2 - 1.05*x**4 + (x**6)/6.0 + x*y + y**2


def trid(X):
    X = _ensure_ndarray(X)
    n = X.shape[-1]
    term1 = np.sum((X - 1.0)**2, axis=-1)
    term2 = np.sum(np.arange(1, n+1) * X, axis=-1)
    return term1 - term2



def wolfe(X):
    X = _ensure_ndarray(X)
    # Wolfe function (simple two-dim variant)
    x = X[...,0]; y = X[...,1]
    return (x + 2*y - 7.0)**2 + (2*x + y - 5.0)**2



def xinsheyangn1(X):
    X = _ensure_ndarray(X)
    # Xin-She Yang N.1
    return np.sum(np.abs(X)**1.0, axis=-1)


def xinsheyangn2(X):
    X = _ensure_ndarray(X)
    return np.sum(np.abs(X)**0.5 + np.power(np.abs(X), 3.0), axis=-1)


def xinsheyangn3(X):
    X = _ensure_ndarray(X)
    return np.sum(X**2, axis=-1) + np.prod(np.abs(X), axis=-1)


def xinsheyangn4(X):
    X = _ensure_ndarray(X)
    return np.sum(X**2, axis=-1) + np.sum(0.5*X, axis=-1)


def zakharov(X):
    X = _ensure_ndarray(X)
    n = X.shape[-1]
    i = np.arange(1, n+1)
    sum1 = np.sum(X**2, axis=-1)
    sum2 = np.sum(0.5*i*X, axis=-1)
    return sum1 + sum2**2 + sum2**4



# funcs_vec: list of (name, function, lower_array, upper_array, known_min)
funcs_vec = [
    ("ackley", ackley, np.full(30,-32.0), np.full(30,32.0), 0),
    ("ackleyn2", ackleyn2, np.full(2,-32.0), np.full(2,32.0), 0),
    ("ackleyn3", ackleyn3, np.full(2,-32.0), np.full(2,32.0), 0),
    ("ackleyn4", ackleyn4, np.full(30,-35.0), np.full(30,35.0), 0),
    ("adjiman", adjiman, np.full(2,-1.0), np.full(2,2.0), -1.0833),
    ("alpinen1", alpinen1, np.full(30,0.0), np.full(30,10.0), 0),
    ("alpinen2", alpinen2, np.full(30,0.0), np.full(30,10.0), -12.0313),
    ("bartelsconn", bartelsconn, np.full(2,-500.0), np.full(2,500.0), 0),
    ("beale", beale, np.full(2,-4.5), np.full(2,4.5), 0),
    ("bird", bird, np.full(2,-6.28318530717959), np.full(2,6.28318530717959), -106.7645),
    ("bohachevskyn1", bohachevskyn1, np.full(2,-100.0), np.full(2,100.0), 0),
    ("bohachevskyn2", bohachevskyn2, np.full(2,-100.0), np.full(2,100.0), 0),
    ("booth", booth, np.full(2,-10.0), np.full(2,10.0), 0),
    ("brent", brent, np.full(2,-20.0), np.full(2,0.0), 0),
    ("brown", brown, np.full(30,-1.0), np.full(30,4.0), 0),
    ("bukinn6", bukinn6, np.full(2,-15.0), np.full(2,3.0), 0),
    ("carromtable", carromtable, np.full(2,-10.0), np.full(2,10.0), -1),
    ("crossintray", crossintray, np.full(2,-10.0), np.full(2,10.0), -2.06261),
    ("deckkersaarts", deckkersaarts, np.full(2,-20.0), np.full(2,20.0), 0),
    ("dropwave", dropwave, np.full(2,-5.2), np.full(2,5.2), -1),
    ("easom", easom, np.full(2,-100.0), np.full(2,100.0), -1),
    ("eggcrate", eggcrate, np.full(2,-5.0), np.full(2,5.0), 0),
    ("elattar", elattar, np.full(2,-500.0), np.full(2,500.0), 0),
    ("exponential", exponential, np.full(30,-1.0), np.full(30,1.0), -1),
    ("forrester", forrester, np.full(1,-0.5), np.full(1,2.5), -6.0207),
    ("goldsteinprice", goldsteinprice, np.full(2,-2.0), np.full(2,2.0), 3),
    ("gramacylee", gramacylee, np.full(1,-0.5), np.full(1,2.5), 0),
    ("griewank", griewank, np.full(30,-600.0), np.full(30,600.0), 0),
    ("happycat", happycat, np.full(30,-2.0), np.full(30,2.0), 0),
    ("himmelblau", himmelblau, np.full(2,-6.0), np.full(2,6.0), 0),
    ("holdertable", holdertable, np.full(2,-10.0), np.full(2,10.0), -19.2085),
    ("keane", keane, np.full(2,0.0), np.full(2,10.0), -0.364),
    ("leon", leon, np.full(2,0.0), np.full(2,10.0), 0),
    ("levin13", levin13, np.full(2,-10.0), np.full(2,10.0), 0),
    ("matyas", matyas, np.full(2,-10.0), np.full(2,10.0), 0),
    ("mccormick", mccormick, np.full(2,-3.0), np.full(2,4.0), -1.9132),
    ("periodic", periodic, np.full(30,-2.0), np.full(30,2.0), 0),
    ("powellsum", powellsum, np.full(30,-1.0), np.full(30,1.0), 0),
    ("qing", qing, np.full(30,-500.0), np.full(30,500.0), 0),
    ("quartic", quartic, np.full(30,-1.28), np.full(30,1.28), 0),
    ("rastrigin", rastrigin, np.full(30,-5.12), np.full(30,5.12), 0),
    ("ridge", ridge, np.full(30,-5.0), np.full(30,5.0), 0),
    ("rosenbrock", rosenbrock, np.full(30,-5.0), np.full(30,10.0), 0),
    ("salomon", salomon, np.full(30,-100.0), np.full(30,100.0), 0),
    ("schaffern1", schaffern1, np.full(2,-100.0), np.full(2,100.0), 0),
    ("schaffern2", schaffern2, np.full(2,-100.0), np.full(2,100.0), 0),
    ("schaffern3", schaffern3, np.full(2,-100.0), np.full(2,100.0), 0),
    ("schaffern4", schaffern4, np.full(2,-100.0), np.full(2,100.0), 0),
    ("schwefel220", schwefel220, np.full(30,-100.0), np.full(30,100.0), 0),
    ("schwefel221", schwefel221, np.full(30,-100.0), np.full(30,100.0), 0),
    ("schwefel222", schwefel222, np.full(30,-100.0), np.full(30,100.0), 0),
    ("schwefel223", schwefel223, np.full(30,-10.0), np.full(30,10.0), 0),
    ("schwefel", schwefel, np.full(30,-500.0), np.full(30,500.0), 0),
    ("shubertn3", shubertn3, np.full(30,-10.0), np.full(30,10.0), -186.7309),
    ("shubertn4", shubertn4, np.full(30,-10.0), np.full(30,10.0), -186.7309),
    ("shubert", shubert, np.full(30,-10.0), np.full(30,10.0), -186.7309),
    ("sphere", sphere, np.full(30,-5.12), np.full(30,5.12), 0),
    ("styblinskitank", styblinskitank, np.full(30,-5.0), np.full(30,5.0), -39.1662),
    ("sumsquares", sumsquares, np.full(30,-10.0), np.full(30,10.0), 0),
    ("threehumpcamel", threehumpcamel, np.full(2,-5.0), np.full(2,5.0), 0),
    ("trid", trid, np.full(30,-2.0), np.full(30,2.0), lambda n: -n*(n+1)*(n+2)//6),
    ("wolfe", wolfe, np.full(3,0.0), np.full(3,2.0), 0),
    ("xinsheyangn1", xinsheyangn1, np.full(30,-5.0), np.full(30,5.0), 0),
    ("xinsheyangn2", xinsheyangn2, np.full(30,-6.28318530717959), np.full(30,6.28318530717959), 0),
    ("xinsheyangn3", xinsheyangn3, np.full(30,-6.28318530717959), np.full(30,6.28318530717959), 0),
    ("xinsheyangn4", xinsheyangn4, np.full(30,-10.0), np.full(30,10.0), 0),
    ("zakharov", zakharov, np.full(30,-5.0), np.full(30,10.0), 0),
]

