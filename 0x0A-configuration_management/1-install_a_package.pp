# installs flask using pip3
package { 'python3':
  ensure   => 'installed'
}

package { 'pip3':
  require  => 'python3',
  ensure   => latest,
  provider => 'pip3',
}

package { 'flask':
  require  => 'python3',
  name     => 'flask',
  ensure   => '2.1.0',
  provider => 'pip3'
}
