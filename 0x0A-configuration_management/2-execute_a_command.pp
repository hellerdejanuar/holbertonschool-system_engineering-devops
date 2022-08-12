# executes pkill to terminate a program
exec { 'kill program':
  command => 'pkill killmenow',
  path    => '/usr/bin'
}
