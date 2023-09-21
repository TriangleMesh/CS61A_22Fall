import sys

from pair import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############


def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Evaluate atoms
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    # All non-atomic expressions are lists (combinations)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    else:
        # BEGIN PROBLEM 3

        # Evaluate all of the operands。并且do not mutate the passed-in "expr"。下面第一种方法是用map函数，Return a new Scheme list after mapping Python function FN to SELF.
        # 错误经验：最后test.scm 540行那个case一直没通过，要注意这个evaluate的顺序，先evaluate operator 然后是 operands
        procedure = scheme_eval(first, env) 
        args = rest.map(lambda x: scheme_eval(x, env))

        # 第二种方法我用了个helper函数，本身我也是照着map函数抄过来的，甚至写的也没有map好，没有handle error情况
        # def helper_eval(args):
        #     if args is nil:
        #         return args
        #     else:
        #         sub_evaled = scheme_eval(args.first,env)
        #         return Pair(sub_evaled, helper_eval(args.rest))
        # args = helper_eval(rest)

        return scheme_apply(procedure, args, env)
        # END PROBLEM 3


def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if not isinstance(env, Frame):
       assert False, "Not a Frame: {}".format(env)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        argsp = []
        while args is not nil:
            argsp.append(args.first)
            args = args.rest
        if procedure.need_env:
            argsp.append(env)
        # END PROBLEM 2
        try:
            # BEGIN PROBLEM 2
            return procedure.py_func(*argsp)
            # END PROBLEM 2
        except TypeError as err:
            raise SchemeError('incorrect number of arguments: {0}'.format(procedure))
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        frame = procedure.env.make_child_frame(procedure.formals, args)
        return eval_all(procedure.body, frame) #错误经验：没写return，eval_all有return，但是这个apply函数还是没有return啊，所以没有返回值报错
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        frame = env.make_child_frame(procedure.formals, args)
        return eval_all(procedure.body, frame)
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)


def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    if expressions is nil:
        return None
    result = scheme_eval(expressions.first, env)
    if expressions.rest is nil:
        return result
    else:
        return eval_all(expressions.rest, env) # 错误经验：这里必须要有return，不然函数没有返回值
    # END PROBLEM 6


##################
# Tail Recursion #
##################

class Unevaluated:
    """An expression and an environment in which it is to be evaluated."""

    def __init__(self, expr, env):
        """Expression EXPR to be evaluated in Frame ENV."""
        self.expr = expr
        self.env = env


def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not an Unevaluated."""
    validate_procedure(procedure)
    val = scheme_apply(procedure, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    else:
        return val


def optimize_tail_calls(unoptimized_scheme_eval):
    """Return a properly tail recursive version of an eval function."""
    def optimized_eval(expr, env, tail=False):
        """Evaluate Scheme expression EXPR in Frame ENV. If TAIL,
        return an Unevaluated containing an expression for further evaluation.
        """
        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Unevaluated(expr, env)

        result = Unevaluated(expr, env)
        # BEGIN PROBLEM EC
        "*** YOUR CODE HERE ***"
        # END PROBLEM EC
    return optimized_eval


################################################################
# Uncomment the following line to apply tail call optimization #
################################################################

# scheme_eval = optimize_tail_calls(scheme_eval)
