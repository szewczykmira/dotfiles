#!/usr/bin/env ruby

puts "Set-up Git"



puts "Git name:"
`git config --global user.name '#{gets.chomp}'`

puts "Git email address:"
`git config --global user.email #{gets.chomp}`

