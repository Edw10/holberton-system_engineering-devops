# kill a process
exec{ 'killmepls':
    command => '/usr/bin/pkill killmenow';
    }