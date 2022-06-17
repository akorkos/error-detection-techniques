function msg = computeParity(x)
  N = length(x);
  countOnes = 0;
  # υπολογίζει το πλήθος των άσσων του μηνύματος
  for i = 1:N
    if (x(i))
      countOnes = countOnes + 1; 
    endif
  endfor 
  if (mod(countOnes, 2) ~= 0) # εξετάζει εάν το πλήθος των άσσων είναι περιττός αριθμός
    msg = [x 1]; # προσθέτει bit ισοτιμίας, με τιμή 1
  else # εξετάζει εάν το πλήθος των άσσων είναι άρτιος αριθμός
    msg = [x 0]; # προσθέτει bit ισοτιμίας, με τιμή 0
  endif
endfunction