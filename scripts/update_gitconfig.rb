`git config --global core.excludesfile ~/.gitignore_global`


puts "Git user name:"
name = gets.chomp

puts "Git user email:"
email = gets.chomp

filename = "/Users/#{`whoami`}/.gitconfig_custom".gsub "\n",""
File.open(filename, "w") {|f| f.write "[user]\n name=#{name}\n email=#{email}"}
