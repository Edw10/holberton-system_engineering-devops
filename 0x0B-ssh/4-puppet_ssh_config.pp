# config the ssh config file
file_line { 'passwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no';
}

file_line { 'add holberton':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton';
}