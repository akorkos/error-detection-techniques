# Συνάρτηση που βρίσκει το πλήθος των άσσων και επιστρέφει τιμή 1 (δηλ. true) 
# μόνο όταν είναι άρτιο πλήθος, καθώς έχουμε άρτια ισοτιμία
function isValid = validateParity(msg)
  N = length(msg);
  countOnes = 0;
  for i = 1:N
    if (msg(i))
      countOnes = countOnes + 1;
    endif
  endfor
  if (mod(countOnes, 2) == 0)
    isValid = 1;
  else
    isValid = 0;
  endif
endfunction