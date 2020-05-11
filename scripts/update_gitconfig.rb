`git config --global core.excludesfile ~/.gitignore_global`


puts "Git user name:"
name = gets.chomp

puts "Git user email:"
email = gets.chomp

File.write("/Users/mira/.gitconfig_custom", "[user]\n name=#{name}\n email=#{email}")
