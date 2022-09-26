# increase ULIMIT traffic bottleneck

# Change defaults file
exec { 'fix-file':
  command => 'sed -i "s/ULIMIT.*/ULIMIT=\"-n 2048\"/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
exec { 'restart':
  command => 'nginx restart',
  path    => 'etc/init.d'
}
