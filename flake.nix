{
  description = "Monitor Utilities for X11";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-21.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in rec {
        packages = flake-utils.lib.flattenTree rec {
          moniutils = pkgs.python3Packages.buildPythonPackage rec {
            name = "moniutils";
            src = ./.;
            propagatedBuildInputs = [
              pkgs.python3Packages.xlib
            ];
          };
        };
        defaultPackage = packages.moniutils;
      });
}
