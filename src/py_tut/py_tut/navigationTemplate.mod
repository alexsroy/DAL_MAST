# This LP aims to solve for the shorest route from the boat's current position to its
# destintation in N steps
# Talk to Claver Diallo or Hamid Afshari in IE if you want to get slides on how LPs work


param n, >=0 default 5; # Number of tacks to consider
set N := 1..n; #Set of tacks


#Basic dimensional variables
var x{i in N}; # Position at end of every tack
var y{i in N};

var dirs{i in N}, binary; # Tack left, or tack right
var magDir1{i in N}, >=0;          # How far to tack
var magDir2{i in N}, >=0;          # How far to tack
var dirChange, binary;
# Unit vector components for x and y
param vectorsX{1, 2};
param vectorsY{1, 2};

# Bounding box parameters
param BBX_upper;
param BBX_lower;
param BBY_upper;
param BBY_lower;


param Boat_x;
param Boat_y;

param startDir;

minimize sail_dist: sum{i in N} magDir1[i] + sum{i in N}magDir2[i] + 0.1 * BBX_upper * dirChange;

# Set start and end positions
s.t. c1: x[1] = Boat_x;
s.t. c2: y[1] = Boat_y;
s.t. c3: x[n] = BBX_upper;
# s.t. c4: y[n] = BBY_upper;

# Confine dimensional positions to the BB
s.t. c5{i in N}: x[i] <= BBX_upper;
s.t. c6{i in N}: BBX_lower <= x[i];
s.t. c7{i in N}: y[i] <= BBY_upper;
s.t. c8{i in N}: BBY_lower <= y[i];

# Update the position
s.t. c9{i in 2 .. n}: x[i] = x[i - 1] + magDir1[i - 1] * vectorsX[1] + magDir2[i - 1] * vectorsX[2];
s.t. c10{i in 2 .. n}: y[i] = y[i - 1] + magDir1[i - 1] * vectorsY[1] + magDir2[i - 1] * vectorsY[2];

# Enforce the binary direction selection DV
s.t. c11{i in N}: magDir1[i] <= 99999 * dirs[i];
s.t. c12{i in N}: magDir2[i] <= 99999 * (1 - dirs[i]);

# Enforce current heading being 1st tack and set up stuff for taking penalty
s.t. c13: dirs[1] = startDir;
s.t. c14: dirChange >= dirs[2] - startDir;
s.t. c15: dirChange >= -dirs[2] + startDir;
#s.t. c14{i in 2..n}: dirs[i - 1] = dirs[i] * (1 - dirChange[i]) + dirChange[i] * (1 - dir[i]);

solve;
display x, y, magDir1, magDir2;
data;

param n := 10;

param BBX_upper := @;
param BBX_lower := 0;
param BBY_upper := ~;
param BBY_lower := -~;

param Boat_x := ^;
param Boat_y := &;

param startDir := _;

param vectorsX :=
1	!
2	$;

param vectorsY :=
1	?
2	%;



end;
