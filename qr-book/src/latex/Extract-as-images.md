The main purpose of the [preview](https://linorg.usp.br/CTAN/macros/latex/contrib/preview/preview.pdf) package is to extract environments as images. To use it, the following line must be added to the preamble of the document.
```latex
\usepackage[active, tightpage]{preview}
```
where options `active` and `tightpage` are specified to activate the package, and to produce separate dimensions for every page, respectively.

The macro `\PreviewEnvironment` sets which environments must produce preview images.
```latex
\PreviewEnvironment{tikzpicture}
\PreviewEnvironment{tabular}
```
The code snippet above, for instance, makes all `tikzpicture` and `tabular` environments in the document produce images.

Full example:
```latex
\documentclass{article}

\usepackage{tikz}
\usepackage[active, tightpage]{preview}
\PreviewEnvironment{tikzpicture}
\PreviewEnvironment{tabular}

\begin{document}

\begin{figure}
    \begin{tikzpicture}
        \draw[step=1cm,gray,very thin] (-1,-1) grid (4,4);

        \draw[thick,->] (0,0) -- (3.5,0);
        \draw[thick,->] (0,0) -- (0,3.5);

        \foreach \x in {0,1,2,3}
            \draw (\x cm,1pt) -- (\x cm,-1pt) node[anchor=north] {$\x$};
        \foreach \y in {0,1,2,3}
            \draw (1pt,\y cm) -- (-1pt,\y cm) node[anchor=east] {$\y$};
    \end{tikzpicture}
\end{figure}

\begin{center}
    \begin{tabular}{ |c|c|c| }
        \hline
        cell1 & cell2 & cell3 \\
        cell4 & cell5 & cell6 \\
        cell7 & cell8 & cell9 \\
        \hline
    \end{tabular}
\end{center}

\end{document}
```
