# create a manifest that kills a process named killmenow using puppet
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/'
}
