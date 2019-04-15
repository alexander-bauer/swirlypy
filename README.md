# Foreword (A Warning)


**Quoting @WilCrofter on Swirlypy, April 09, 2019, in response to a
recetly-opened issue:**
> Swirlypy was a initial prototype created one afternoon by
> @alexander-bauer at the behest of @WilCrofter (me) and @reginaastri,
> two of the original [swirl](https://swirlstats.com/) developers. We
> have never followed up on swirlypy and, other than proof-of-concept
> material, there is no real course material associated with it.
>
> We left the prototype up on GitHub in case a future developer wanted to
> follow up. Swirl's lead developer, @seankross, has expressed interest in
> that possibility, but the likely candidates have been preoccupied with other
> Projects.
>
> Swirl itself is currently a very mature project with a
> [great deal](http://swirlstats.com/scn/) of
> [course material](https://github.com/swirldev/swirl_courses#swirl-courses).
> Swirl uses the R programming language and emphasizes statistics and data
> science. 
>
> If you are primarily interested in interactive coursework and not committed
> to Python, I'd suggest looking into swirl.
>
> If you are committed to Python and primarily interested in course material,
> I'd suggest looking into [Jupyter](https://jupyter.org/) beginning with the
> examples at [Binder](https://mybinder.readthedocs.io/en/latest/examples.html)
> which can be used in a browser.)
>
> Of course you are welcome to pick up swirlypy as a developer, but I would
> again suggest looking a Swirl or Jupyter first.

As of this writing in April of 2019, Swirlypy is a proof-of-concept that
has been left undeveloped for a handful of years. Though it and the Swirl
project that it was inspired by have been important in my life, I can no longer
claim to be an active maintainer of Swirlypy.

For any developers who are interested in the prospect of continuing Swirlypy
where I have left it off, I am still alive and well, and available through
GitHub and email to answer questions and justify my design choices. The code,
though dense in some places, is commented reasonably well, and engineered
initially with extensibility in mind. (Perhaps it was over-engineered and
over-designed. Only time would tell.)

---

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

## Running a Course

For the purposes of development and testing, it is possible to run Swirlypy in
a Python3 virtual environment. These are some steps, from the repository root:

```
virtualenv -p python3 env
env/bin/pip install --editable .

env/bin/swirlytool run courses/intro
```

If you activate the virtual environment with `env/bin/activate`, you won't need
to specify `env/bin/` before `pip` or `swirlytool`.

**Note**: Remember to specify the containing directory, not `course.yaml`, for
unpackaged courses.

### Course Data

The `course.yaml` file must be present in the root of the course, and
contain the following fields: `course` (course title),
`lessonnames` (list of human-readable lesson names), and `author` (human
readable author name or names). It may also contain: `description`
(explanatory text), `organization` (name of the course's sponsoring
organization), `version` (a string, usually of numbers), and `published`
(a timestamp in YAML format). An example is available
[here][intro_courseyaml].

### Lesson files

Lessons are YAML files contained in the `lessons/` subdirectory. Their
filenames are "sluggified," meaning that all non-ascii characters are
replaced by dashes, and all ascii characters are lowercased. For
example, a lesson called "Basics in Statistics" will be in a file named
`basics-in-statistics.yaml`.

Each lesson is, itself, simply a list (what YAML calls a sequence) of
questions. Fields at the root of lessons are not case sensitive, and an
example lesson can be seen [here][intro_lessonyaml].

### Questions

Questions are, under the hood, all descended from a particular Python
class. As such, they share certain properties, including the way they
are parsed from YAML. Fields at the root are not case sensitive, and
they are used as keyword arguments to construct Questions matching the
listed category. For example, a Question of the "text" category will
construct a TextQuestion.

The exact fields required by each question are determined by the type of
question, but they at least require `Category` and `Output`. All of the
questions in the standard library can be found [here][question_stdlib].

Furthermore, new questions can be defined within courses by placing them
within a `questions` subdirectory, the same as with the standard
library.

### Packaging your Course

The `swirlytool` application that comes with Swirlypy is capable of
packaging a course by using the `create` subcommand. This produces a
Swirlypy course file, which is just a gzipped tar file with a particular
format.

[intro_courseyaml]: courses/intro/course.yaml
[intro_lessonyaml]: courses/intro/lessons/values-types-and-variables.yaml
[question_stdlib]: swirlpy/questions/
