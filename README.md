company-netlogo
===============

This is a backend for `company-mode` which provides auto-completion for netlogo. This is currently a Work-In-Progress, but works. The list of functions is compiled directly from the [Netlogo Dictionary](https://ccl.northwestern.edu/netlogo/docs/dictionary.html). It is possible to select which functions are wanted by modifying the XPath statements in `generate-meta.py`.

## Usage


    ;; install somewhere on your load path
    (require 'company-netlogo)
    (add-to-list 'company-backends 'company-netlogo)
    ;; or when using multiple backends -- this preserves sorting despite fuzzy completion
    (add-to-list 'company-backends '(:separate company-netlogo company-yasnippet ...))
    


## Configuration

The package has the following options so far:

 * `company-netlogo-fuzzy`
   * This is normally `t`, indicating that the backend will use substring matching. When this is enabled, typing `xy` will provide both _setxy_ and _distancexy_ despite neither of them actually starting with `xy`.

