#correct the 500 error
file_line { 'replace':
  path    => '/var/www/html/wp-settings.php',
  replace => true,
  line    => 'require_once( ABSPATH . WPINC . "/class-wp-locale.php" );',
  match   => 'require_once( ABSPATH . WPINC . "/class-wp-locale.phpp" );'
}
