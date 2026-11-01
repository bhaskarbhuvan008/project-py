[33mcommit 7ab5725ab0ce47bfaae4d9c5c3022bc59569cc54[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mmain[m[33m, [m[1;31morigin/main[m[33m)[m
Author: bhaskarbhuvan008 <bhaskarbhuvan008@gmail.com>
Date:   Wed Oct 28 00:29:18 2026 +0530

    fix

[1mdiff --git a/.gitignore b/.gitignore[m
[1mindex 8e819cb..5987609 100644[m
[1m--- a/.gitignore[m
[1m+++ b/.gitignore[m
[36m@@ -1,3 +1,5 @@[m
 *.csv[m
 *.xlsx[m
 .env[m
[32m+[m
[32m+[m[32m__pycache__/[m
\ No newline at end of file[m
[1mdiff --git a/cleaners_common.py b/cleaners_common.py[m
[1mindex 3e63af8..69903f5 100644[m
[1m--- a/cleaners_common.py[m
[1m+++ b/cleaners_common.py[m
[36m@@ -6,7 +6,7 @@[m [mdef clean_gender(series):[m
             "MALE":"M",[m
             "FEMALE":"F"[m
             })[m
[31m-    clean = clean.where(clean.isin(["M","S",""]),"U")[m
[32m+[m[32m    clean = clean.where(clean.isin(["M","F",""]),"U")[m
 [m
     return clean[m
 [m
