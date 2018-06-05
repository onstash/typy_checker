"""
Module that checks for types in methods.
Exposes a decorator that does basic type checking for function arguments.
Raises a SystemError when it encounters a type mismatch.
"""
__all__ = ("type_checker",)
__author__ = "Santosh Venkatraman<santosh.venk@gmail.com>"

import sys
sys.dont_write_bytecode = True


def type_checker(**arguments_types):
    """
    Main decorator that takes in a dict {variable:type} to run type checks
    for arguments.

    :param arguments_types: Dict containing type information
    :type  arguments_types: dict
    """
    def decorator(function):
        """
        Inner decorator to work with the decorated/wrapped function
        """
        def wrapper(*args, **kwargs):
            """
            Function wrapper that checks arguments against given types
            """
            function_name = "{}()".format(function.__name__)
            types_error = " ".join([
                "{}: Keyword arguments of variables &",
                "respective types must be provided.",
                "\nUsage: @type_checker(foo=int, bar=float)"
            ]).format(function_name)

            if not arguments_types:
                raise SystemError(types_error)

            if not isinstance(arguments_types, dict):
                raise SystemError(
                    types_error
                )

            filtered_arguments_types = {
                variable: variable_type
                for variable, variable_type in arguments_types.items()
                if isinstance(variable_type, type) or \
                all([isinstance(x, type) for x in variable_type])
            }

            if not filtered_arguments_types:
                raise SystemError(types_error)

            args_count_mismatch_error = \
                "{}: requires {} argument{}. {} {} provided."
            args_count = len(args)
            kwargs_count = len(kwargs)

            required_args_count = function.__code__.co_argcount
            if (args_count + kwargs_count) != required_args_count:
                raise SystemError(
                    args_count_mismatch_error.format(
                        function_name,
                        required_args_count,
                        "" if required_args_count == 1 else "s",
                        args_count,
                        "was" if args_count == 1 else "were",
                    )
                )

            _kwargs = dict(zip(function.__code__.co_varnames, args))
            _kwargs.update(**kwargs)

            types_count_mismatch_error = \
                "{}: {} type{} {} provided for {} args/kwargs"

            types_count = len(filtered_arguments_types)
            kwargs_count = len(_kwargs)

            if types_count != kwargs_count:
                is_types_count_one = types_count == 1
                raise SystemError(
                    types_count_mismatch_error.format(
                        function_name,
                        types_count,
                        "" if is_types_count_one else "s",
                        "was" if is_types_count_one else "were",
                        kwargs_count
                    )
                )
            
            invalid_type_error = " ".join([
                "{}: Invalid type for variable",
                "'{}'. Expected {}",
                "but got {}."
            ])

            valid_meta_types = (list, tuple)

            for argument_key, argument_value in _kwargs.items():
                expected_type = filtered_arguments_types.get(argument_key)
                expected_types = expected_type \
                    if isinstance(expected_type, valid_meta_types) \
                    else (expected_type,)
                if not isinstance(argument_value, expected_types):
                    raise SystemError(
                        invalid_type_error.format(
                            function_name,
                            argument_key,
                            " / ".join([
                                "{}".format(_expected_type.__name__)
                                for _expected_type in expected_types
                            ]),
                            type(argument_value).__name__
                        )
                    )
            return function(*args, **kwargs)
        return wrapper
    return decorator
