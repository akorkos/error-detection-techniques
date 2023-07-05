function msg = compute2dParity(msg, N, M)
	% μετράει των αριθμό των άσσων κάθε γραμμής
	for i = 1 : N
	  countOnes = 0;
	  for j = 1 : M
		if (msg(i ,j))
		  countOnes = countOnes + 1;
		end
	  end
	  if (mod(countOnes, 2) == 0) % σε περίπτωση που είναι άρτιος, 
		% προσθέτει σε μια νέα στήλη με δείκτη (i, M + 1) ένα μηδενικό
		msg(i, M + 1) = 0;
	  else % διαφορετικά προσθέτει 1
		msg(i, M + 1) = 1;
	  end
	end

	% μετράει των αριθμό των άσσων κάθε στήλης
	for i = 1 : M + 1
	  countOnes = 0;
	  for j = 1 : N
		if (msg(j, i))
		  countOnes = countOnes + 1;
		end
	  end
	  if (mod(countOnes, 2) == 0) % σε περίπτωση που είναι άρτιος, 
		% προσθέτει σε μια νέα γραμμή με δείκτη (N + 1, i) ένα μηδενικό
		msg(N + 1, i) = 0;
	  else % διαφορετικά προσθέτει 1
		msg(N + 1, i) = 1;
	  end
	end
end
