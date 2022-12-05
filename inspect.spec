Name: inspect
Version: {{{ git_dir_version }}}
Release: 1%{?dist}
Summary: Human-readable representation of Lua tables
License: MIT

Source: {{{ git_dir_pack }}}

Url: https://github.com/Rosettea/inspect.lua
VCS: {{{ git_dir_vcs }}}
BuildArch: noarch

%description
This library transforms any Lua value into a human-readable representation. It is especially useful for debugging errors in tables.
The objective here is human understanding (i.e. for debugging), not serialization or compactness.

%prep
{{{ git_dir_setup_macro }}}

%build

%install
install -Dm644 inspect.lua -t %{buildroot}/usr/share/hilbish/libs/inspect/

%files
%doc README.md
%license MIT-LICENSE.txt
/usr/share/hilbish/libs/inspect/inspect.lua
