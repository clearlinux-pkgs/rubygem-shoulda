#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-shoulda
Version  : 3.5.0
Release  : 4
URL      : https://rubygems.org/downloads/shoulda-3.5.0.gem
Source0  : https://rubygems.org/downloads/shoulda-3.5.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-cucumber
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec-rails

%description
# shoulda [![Gem Version](https://badge.fury.io/rb/shoulda.png)](http://badge.fury.io/rb/shoulda) [![Build Status](https://secure.travis-ci.org/thoughtbot/shoulda.png)](http://travis-ci.org/thoughtbot/shoulda)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n shoulda-3.5.0
gem spec %{SOURCE0} -l --ruby > rubygem-shoulda.gemspec

%build
gem build rubygem-shoulda.gemspec

%install
gem_dir=$(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .${gem_dir} \
--bindir .%{_bindir} \
shoulda-3.5.0.gem

mkdir -p %{buildroot}${gem_dir}
cp -pa .${gem_dir}/* \
%{buildroot}${gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/shoulda-3.5.0.gem
/usr/lib64/ruby/gems/2.2.0/doc/shoulda-3.5.0/ri/Shoulda/cdesc-Shoulda.ri
/usr/lib64/ruby/gems/2.2.0/doc/shoulda-3.5.0/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/.autotest
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/.travis.yml
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/Appraisals
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/MIT-LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/README.md
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/features/rails_integration.feature
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/features/step_definitions/rails_steps.rb
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/features/support/env.rb
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/gemfiles/3.0.gemfile
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/gemfiles/3.0.gemfile.lock
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/gemfiles/3.1.gemfile
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/gemfiles/3.1.gemfile.lock
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/gemfiles/3.2.gemfile
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/gemfiles/3.2.gemfile.lock
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/lib/shoulda.rb
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/lib/shoulda/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/shoulda-3.5.0/shoulda.gemspec
/usr/lib64/ruby/gems/2.2.0/specifications/shoulda-3.5.0.gemspec
