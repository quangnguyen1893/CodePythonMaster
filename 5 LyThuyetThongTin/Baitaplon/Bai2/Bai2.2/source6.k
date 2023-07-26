{
	int i;
	i = 10;
	while i > 20 do
		print(i);
	endo
	int j;
	j = i + 15;
	if j > 20 then
		while j >= 20 do
			print(j);
			j = j - 1;
		endo
	endif
	print(j);
	if i != j then
		j = i;
		if i == j then
			print(i);
			print(j);
		endif
	endif
}
