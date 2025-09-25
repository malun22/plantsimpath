from pathlib import Path
from typing import Union, Iterator, List


class PlantsimPath:
    """
    PlantSim path object for handling and concatenating hierarchical object paths.

    :param entries: Entries to be concatenated into a path.
    :type entries: Union[str, PlantsimPath]

    :ivar _path: Internal string representation of the path.
    :vartype _path: str
    """

    def __init__(self, *entries: Union[str, "PlantsimPath"]) -> None:
        """
        Initialize a PlantsimPath by concatenating given entries.

        :param entries: Strings or PlantsimPath objects to build the path.
        :type entries: Union[str, PlantsimPath]
        """
        self._path: str = ""
        for entry in entries:
            if isinstance(entry, PlantsimPath):
                entry = str(entry)
            self.append(entry)

    def __str__(self) -> str:
        """
        Return the path as a string.

        :return: Path as string.
        :rtype: str
        """
        return self._path

    def __repr__(self) -> str:
        """
        Return the official string representation of the object.

        :return: Representation string.
        :rtype: str
        """
        return f"PlantsimPath('{self._path}')"

    def __eq__(self, other) -> bool:
        """
        Compare two PlantsimPath objects.

        :param other: Object to compare against.
        :type other: Any
        :return: True if paths are equal, False otherwise.
        :rtype: bool
        """
        if not isinstance(other, PlantsimPath):
            return False
        return str(self) == str(other)

    def __hash__(self) -> int:
        """
        Return a hash value of the path.

        :return: Hash value.
        :rtype: int
        """
        return hash(self._path)

    def __add__(self, other: Union[str, "PlantsimPath"]) -> "PlantsimPath":
        """
        Concatenate two paths using the + operator.

        :param other: String or PlantsimPath to append.
        :return: New PlantsimPath instance.
        """
        return PlantsimPath(self, other)

    def __truediv__(self, other: Union[str, "PlantsimPath"]) -> "PlantsimPath":
        """
        Concatenate two paths using the / operator.

        :param other: String or PlantsimPath to append.
        :return: New PlantsimPath instance.
        """
        return PlantsimPath(self, other)

    def __iter__(self) -> Iterator[str]:
        """
        Allow iteration over path segments.

        :return: Iterator over path segments.
        """
        return iter(self.parts())

    def parts(self) -> List[str]:
        """
        Split the path into its segments.

        :return: List of path parts.
        """
        path = self._path.lstrip(".")
        parts, buf, bracket = [], "", 0
        for c in path:
            if c == "[":
                bracket += 1
            elif c == "]":
                bracket -= 1
            if c == "." and bracket == 0:
                parts.append(buf)
                buf = ""
            else:
                buf += c
        if buf:
            parts.append(buf)
        return parts

    def parent(self) -> "PlantsimPath":
        """
        Get the parent path.

        :return: Parent PlantsimPath.
        """
        parts = self.parts()
        if len(parts) <= 1:
            return PlantsimPath()
        return PlantsimPath(*parts[:-1])

    def is_child_of(self, other: "PlantsimPath") -> bool:
        """
        Check if self is a child of other.

        :param other: Parent path.
        :return: True if self is a child of other.
        """
        return str(self).startswith(str(other)) and str(self) != str(other)

    def is_empty(self) -> bool:
        """
        Check if the path is empty.

        :return: True if path is empty, else False.
        """
        return not self._path

    def append(self, entry: str) -> None:
        """
        Append a path entry to the current path.

        :param entry: Path entry to append.
        :type entry: str
        """
        if not entry:
            return
        # Basic validation: no forbidden characters
        if "\n" in entry or "\r" in entry:
            raise ValueError(
                "Path entries cannot contain newline or carriage return characters."
            )
        elif entry.startswith(".") or entry.startswith("[") or self._path.endswith("."):
            self._path += entry
        else:
            self._path += f".{entry}"

    def to_str(self) -> str:
        """
        Return the path as a string.

        :return: Path as string.
        :rtype: str
        """
        return str(self)

    def to_path(self) -> Path:
        """
        Convert the PlantsimPath to a pathlib Path object.

        :return: pathlib.Path object.
        """
        return Path(*self.parts())

    def to_folder_path(self) -> Path:
        """
        Convert the PlantsimPath to a pathlib Path object referring to the meta data of a folder / frame.

        :return: pathlib.Path object.
        """
        return Path(*self.parts(), "$").with_suffix(".yaml")

    def to_object_path(self) -> Path:
        """
        Convert the PlantsimPath to a pathlib Path object referring to the meta data of an object.

        :return: pathlib.Path object.
        """
        return Path(*self.parts()).with_suffix(".yaml")

    @classmethod
    def from_path(cls, path: Union[Path, str]) -> "PlantsimPath":
        """
        Create a PlantsimPath from a pathlib.Path or string.

        :param path: Path object or string.
        :return: PlantsimPath instance.
        """
        if isinstance(path, str):
            path = Path(path)
        return cls(*[str(part) for part in path.parts])
