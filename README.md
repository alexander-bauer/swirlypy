## For Developers

swirlypy is a Python package, meaning that its directory must be
located somewhere in your Python path. For individuals with sane
directory structures, this likely means temporarily adding the path to
the directory above swirlypy's to your `$PYTHONPATH`. Alternatively,
you could add a symlink from an existing Python directory. Eventually,
we should be able to install swirlypy as a package and avoid this issue,
but for the moment this is the workaround.

## Creating a Course

Swirlypy courses are distributed as tar archives (compressed or not)
with a particular directory structure. They are required to have a
`course.yaml` file, which describes the course in general. In addition,
they must contain a `lessons` directory, with lesson files (see below).

### Course Data

The `course.yaml` file must be present in the root of the course, and
contain the following fields: `course` (course title),
`lessonnames` (list of human-readable lesson names), and `author` (human
readable author name or names). It may also contain: `description`
(explanatory text), `organization` (name of the course's sponsoring
organization), `version` (a string, usually of numbers), and `published`
(a timestamp in YAML format).
