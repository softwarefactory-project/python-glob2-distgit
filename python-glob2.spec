%global sum     Version of the glob module that supports recursion via **, and can capture patterns.

Name:           python-glob2
Version:        0.5
Release:        1%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://github.com/miracle2k/python-glob2/
Source0:        https://github.com/miracle2k/python-glob2/archive/v%{version}.tar.gz

BuildArch:      noarch


%description
This is an extended version of Python's builtin glob module (http://docs.python.org/library/glob.html) which adds:

* The ability to capture the text matched by glob patterns, and return those matches alongside the filenames.
* A recursive '**' globbing syntax, akin for example to the globstar option of the bash shell.
* The ability to replace the filesystem functions used, in order to glob on virtual filesystems.
* Compatible with Python 2 and Python 3 (tested with 3.3).


%package -n python2-glob2
Summary:        %sum

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       python-setuptools


%description -n python2-glob2
This is an extended version of Python's builtin glob module (http://docs.python.org/library/glob.html) which adds:

* The ability to capture the text matched by glob patterns, and return those matches alongside the filenames.
* A recursive '**' globbing syntax, akin for example to the globstar option of the bash shell.
* The ability to replace the filesystem functions used, in order to glob on virtual filesystems.
* Compatible with Python 2 and Python 3 (tested with 3.3).


%prep
%autosetup -n %{name}-%{version}


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc CHANGES
%license LICENSE


%files -n python2-glob2
%{python2_sitelib}/glob2-%{version}-py*.egg-info
%{python2_sitelib}/glob2


%changelog
* Tue Feb 21 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 0.5-1
- Initial packaging
