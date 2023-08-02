#!/usr/bin/env ruby
# The script outputs [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/\[from:(\+?\w*)\]\s\[to:(\+?\w*)\]\s\[flags:(\S*)\]/).join(',')
