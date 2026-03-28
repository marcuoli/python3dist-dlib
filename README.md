# python3dist(dlib) Fedora 43 RPM

This workspace contains a starter Fedora spec for building `python3dist(dlib)`.

## Files

- `SPECS/python3-dlib.spec`: RPM spec file
- `SOURCES/`: source tarballs (if you build with plain `rpmbuild`)

## Option A: Build with mock (recommended)

Install tools:

```bash
sudo dnf install -y fedora-packager rpmdevtools mock
```

Build SRPM from the spec and automatically fetch source from `Source0`:

```bash
cd /run/media/marcuoli/Ventoy/python3dist\(dlib\)
mock -r fedora-43-x86_64 --buildsrpm --spec SPECS/python3-dlib.spec --sources SOURCES
```

Build binary RPM:

```bash
mock -r fedora-43-x86_64 --rebuild /var/lib/mock/fedora-43-x86_64/result/python3-dlib-*.src.rpm
```

Resulting RPMs are placed under:

```bash
/var/lib/mock/fedora-43-x86_64/result/
```

## Option B: Build locally with rpmbuild

Set up your rpmbuild tree once:

```bash
rpmdev-setuptree
```

Copy spec into rpmbuild tree:

```bash
cp SPECS/python3-dlib.spec ~/rpmbuild/SPECS/
```

Download source tarball expected by the spec:

```bash
spectool -g -R ~/rpmbuild/SPECS/python3-dlib.spec --define "_topdir $HOME/rpmbuild"
```

Build:

```bash
rpmbuild -ba ~/rpmbuild/SPECS/python3-dlib.spec
```

Artifacts will be under:

- `~/rpmbuild/SRPMS/`
- `~/rpmbuild/RPMS/`

## Notes

- dlib builds native C++ extensions; build time can be significant.
- If you need GUI support in dlib, remove `DLIB_NO_GUI_SUPPORT=1` in the spec and add required X11 deps.
- Version can be updated by editing `Version:` in the spec.
