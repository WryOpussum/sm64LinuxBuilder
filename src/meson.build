pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'sm64linuxbuilder')




python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'sm64linuxbuilder.in',
  output: 'sm64linuxbuilder',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

sm64linuxbuilder_sources = [
  'main.py',
]

install_data(sm64linuxbuilder_sources, install_dir: moduledir)
