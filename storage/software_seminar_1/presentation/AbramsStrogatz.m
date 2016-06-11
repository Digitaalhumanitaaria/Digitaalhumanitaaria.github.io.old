% A program to solve ODE model for Language survival
% This uses Forward Euler
% D.M. Abrams, S.H. Strogatz 
% ``Modelling the dynamics of language death''
% Nature 424 pp. 900 (2013)
% http://dx.doi.org/10.1088/1367-2630/13/3/033007

% The program should run in Octave https://www.gnu.org/software/octave/
% or Matlab http://se.mathworks.com/products/matlab/?requestedDomain=www.mathworks.com
% Reproduce results from Figure 5
clear all; format compact; format short;
set(0,'defaultaxesfontsize',30,'defaultaxeslinewidth',.7,...
    'defaultlinelinewidth',6,'defaultpatchlinewidth',3.7,...
    'defaultaxesfontweight','bold')

fig="c";

dt=0.01; % timestep
Nt=10^4; % number of timesteps
a=1.31;  % model parameter
T(1)=0;  % array of times solution is approximated at
c=1;     % time scaling constant

switch fig
 case{"a"}
   s=0.33; X(1)=0.84; Y(1)=1-X(1);
 case{"b"}
   s=0.26; X(1)=0.68; Y(1)=1-X(1);
 case{"c"}
   s=0.40; X(1)=0.87; Y(1)=1-X(1);
 case{"d"}
   s=0.43; X(1)=0.5; Y(1)=1-X(1);
 otherwise
 display("invalid value");
endswitch

for n = 2:Nt+1
 Pyx=c*s*(X(n-1))^a;
 Pxy=c*(1-s)*(1-X(n-1))^a;
 X(n)=X(n-1)+dt*(Y(n-1)*Pyx-X(n-1)*Pxy);
 Y(n)=1-X(n);
 T(n)=T(n-1)+dt;
end
figure(1); clf; plot(T,X,'r-',T,Y,'g-');
