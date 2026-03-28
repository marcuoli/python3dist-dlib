# Fedora 43 RPMs for Howdy dependencies

This workspace contains Fedora spec files for building the dependencies needed to run Howdy on Fedora 43:

- `python3dist(dlib)`
- `pam_python`

## Why this exists

This work was done to make it possible to run **Howdy** on Fedora 43, where installation can fail when `python3dist(dlib)` is not available in the required version.

### Error observed when installing Howdy on Fedora 43

The hostname below was redacted for privacy.

```text
root@fedora43:/mnt# dnf --refresh install howdy
Atualizando e carregando repositórios:
 RPM Fusion for Fedora 43 - Nonfree - Steam                                                                                                                                                                                                        100% |   2.4 KiB/s |  15.1 KiB |  00m06s
 RPM Fusion for Fedora 43 - Nonfree - NVIDIA Driver                                                                                                                                                                                                100% |   3.7 KiB/s |  16.3 KiB |  00m04s
 Fedora 43 - x86_64 - Updates                                                                                                                                                                                                                      100% |   2.4 KiB/s |   8.6 KiB |  00m04s
 Copr repo for PyCharm owned by phracek                                                                                                                                                                                                            100% |   1.5 KiB/s |   2.1 KiB |  00m01s
 google-chrome                                                                                                                                                                                                                                     100% | 952.0   B/s |   1.3 KiB |  00m01s
 Fedora 43 - x86_64                                                                                                                                                                                                                                100% |  22.8 KiB/s |  60.0 KiB |  00m03s
 Copr repo for howdy owned by principis                                                                                                                                                                                                            100% |   1.1 KiB/s |   1.5 KiB |  00m01s
 Fedora 43 openh264 (From Cisco) - x86_64                                                                                                                                                                                                          100% | 527.0   B/s | 986.0   B |  00m02s
Repositórios carregados.
Falha ao resolver a transação:
Problema: solicitações conflitantes
	- nada fornece python3dist(dlib) >= 6.0 necessário por howdy-2.6.1-10.fc43.x86_64 de copr:copr.fedorainfracloud.org:principis:howdy
Você pode tentar adicionar à linha de comando:
	--skip-broken para ignorar pacotes desinstaláveis
root@fedora43:/mnt#
```

This repository addresses that dependency gap by providing a Fedora 43 build path for both required packages.

## Files

- `SPECS/python3-dlib.spec`: RPM spec for dlib
- `SPECS/pam_python.spec`: RPM spec for pam_python
- `~/rpmbuild/SOURCES/python-pam-1.0.8.tar.gz`: source tarball used by `pam_python.spec`

## Quick install using already-built RPMs

If you already built the packages, install them first and then install Howdy:

```bash
sudo dnf install -y \
	~/rpmbuild/RPMS/x86_64/python3-dlib-19.24.6-1.fc43.x86_64.rpm \
	~/rpmbuild/RPMS/x86_64/pam_python-1.0.8-4.fc43.x86_64.rpm

sudo dnf install -y howdy
```

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

Build `pam_python`:

```bash
rpmbuild -ba ~/rpmbuild/SPECS/pam_python.spec
```

Artifacts will be under:

- `~/rpmbuild/SRPMS/`
- `~/rpmbuild/RPMS/`

Expected artifacts after a successful build:

- `~/rpmbuild/SRPMS/python3-dlib-19.24.6-1.fc43.src.rpm`
- `~/rpmbuild/RPMS/x86_64/python3-dlib-19.24.6-1.fc43.x86_64.rpm`
- `~/rpmbuild/SRPMS/pam_python-1.0.8-4.fc43.src.rpm`
- `~/rpmbuild/RPMS/x86_64/pam_python-1.0.8-4.fc43.x86_64.rpm`

## Install Howdy after building

```bash
sudo dnf install -y \
	~/rpmbuild/RPMS/x86_64/python3-dlib-*.rpm \
	~/rpmbuild/RPMS/x86_64/pam_python-*.rpm

sudo dnf install -y howdy
```

## Notes

- dlib builds native C++ extensions; build time can be significant.
- If you need GUI support in dlib, remove `DLIB_NO_GUI_SUPPORT=1` in the spec and add required X11 deps.
- Version can be updated by editing `Version:` in the spec.
