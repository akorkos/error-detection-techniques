function msg = computeParity(x)
  N = length(x);
  countOnes = 0;
  for i = 1:N
    if (x(i))
      countOnes = countOnes + 1;
    endif
  endfor 
  if (mod(countOnes, 2) ~= 0)
    msg = [x 1];
  else
    msg = [x 0];
  endif
endfunction