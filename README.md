# arxiv_scraper
Scraper for arxiv preprints. Simple aggregation of calls to the Arxiv REST-api.

## Usage
<pre><font color="#008700">In [</font><font color="#8AE234"><b>1</b></font><font color="#008700">]: </font><font color="#008700"><b>import</b></font> <font color="#0087D7"><b>arxiv_scraper</b></font> <font color="#008700"><b>as</b></font> <font color="#0087D7"><b>AS</b></font>

<font color="#008700">In [</font><font color="#8AE234"><b>2</b></font><font color="#008700">]: </font>AS.get(<font color="#AF5F00">&apos;Hesselholt&apos;</font>)
Fetching preprints...
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████| 10/10 [00:07&lt;00:00,  1.29it/s]
Done

<font color="#008700">In [</font><font color="#8AE234"><b>3</b></font><font color="#008700">]: </font>ls Hesselholt
&apos;Algebraic K-theory and trace invariants.tex&apos;
&apos;Bi-relative algebraic K-theory and topological cyclic homology.tex&apos;
&apos;On the K-theory of planar cuspical curves and a new family of polytopes.tex&apos;
&apos;On the K-theory of the coordinate axes in the plane.tex&apos;
&apos;On the Whitehead spectrum of the circle.tex&apos;
&apos;On the topological cyclic homology of the algebraic closure of a local&apos;$&apos;\n&apos;&apos;  field.tex&apos;
&apos;The big de Rham-Witt complex.tex&apos;
&apos;The de Rham-Witt complex and p-adic vanishing cycles.tex&apos;
&apos;The tower of K-theory of truncated polynomial algebras.tex&apos;
&apos;Topological Hochschild homology and the Hasse-Weil zeta function.tex&apos;</pre>
