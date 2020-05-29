#change user limit
exec { 'change limit':
  provider  => shell,
  command   => 'sed -i "s/4/1000/g" /etc/security/limits.conf',
  }