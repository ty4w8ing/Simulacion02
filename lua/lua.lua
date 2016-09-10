-- comentarios con --
i = 1000000
file = io.open("lua.txt", "w+")
while( i ~= 0 ) do
   file:write(string.format("%.10f", math.random()) .. "\n")
   i = i-1
end
file:close()