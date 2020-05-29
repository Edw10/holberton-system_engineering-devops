#change the limit of request lenght
exec { 'high af':
  provider => shell,
  command  => 'sed -i "s/15/2000/g" /etc/default/nginx',
}
exec { 'apply changes':
  provider => shell,
  command  => 'sudo service nginx restart',
}