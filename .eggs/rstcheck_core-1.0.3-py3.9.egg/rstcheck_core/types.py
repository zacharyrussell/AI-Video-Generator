"""Helper types."""
import pathlib
import typing as t

from . import _compat as _t


SourceFileOrString = t.Union[pathlib.Path, _t.Literal["<string>"], _t.Literal["<stdin>"]]
"""Path to source file or if it is a string then '<string>' or '<stdin>'."""


class LintError(_t.TypedDict):
    """Dict with information about an linting error."""

    source_origin: SourceFileOrString
    line_number: int
    message: str


YieldedLintError = t.Generator[LintError, None, None]
"""Yielded version of type :py:class:`LintError`."""


class IgnoreDict(_t.TypedDict):
    """Dict with ignore information."""

    # NOTE: Pattern type-arg errors pydanic: https://github.com/samuelcolvin/pydantic/issues/2636
    messages: t.Optional[t.Pattern]  # type: ignore[type-arg]
    languages: t.List[str]
    directives: t.List[str]
    roles: t.List[str]
    substitutions: t.List[str]


def construct_ignore_dict(
    # NOTE: Pattern type-arg errors pydanic: https://github.com/samuelcolvin/pydantic/issues/2636
    messages: t.Optional[t.Pattern] = None,  # type: ignore[type-arg]
    languages: t.Optional[t.List[str]] = None,
    directives: t.Optional[t.List[str]] = None,
    roles: t.Optional[t.List[str]] = None,
    substitutions: t.Optional[t.List[str]] = None,
) -> IgnoreDict:
    """Create an :py:class:`IgnoreDict` with passed values or defaults.

    :param messages: Value for :py:attr:`IgnoreDict.messages`;
        :py:obj:`None` results in an empty list; defaults to :py:obj:`None`
    :param directives: Value for :py:attr:`IgnoreDict.directives`;
        :py:obj:`None` results in an empty list; defaults to :py:obj:`None`
    :param roles: Value for :py:attr:`IgnoreDict.roles`;
        :py:obj:`None` results in an empty list; defaults to :py:obj:`None`
    :param substitutions: Value for :py:attr:`IgnoreDict.substitutions`;
        :py:obj:`None` results in an empty list; defaults to :py:obj:`None`
    :return: :py:class:`IgnoreDict` with passed values or defaults
    """
    return IgnoreDict(
        messages=messages,
        languages=languages if languages is not None else [],
        directives=directives if directives is not None else [],
        roles=roles if roles is not None else [],
        substitutions=substitutions if substitutions is not None else [],
    )


CheckerRunFunction = t.Callable[..., YieldedLintError]
"""Function to run checks.

Returned by :py:meth:`rstcheck_core.checker.CodeBlockChecker.create_checker`.
"""


class InlineConfig(_t.TypedDict):
    """Dict with a config key and config value comming from a inline config comment."""

    key: str
    value: str


class InlineFlowControl(_t.TypedDict):
    """Dict with a flow control value and line number comming from a inline config comment."""

    value: str
    line_number: int
