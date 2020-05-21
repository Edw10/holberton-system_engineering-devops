#correct the 500 error
exec {'change line':
  provider => shell,
  command  => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
}