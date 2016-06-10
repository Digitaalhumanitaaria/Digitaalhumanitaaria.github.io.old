% M. Patriarca and E. Heinsalu ``Influence of geography on language competition''
% http://arxiv.org/abs/0807.3100v2
% Solve 
% N1_t = k(s1 N1^a N2 - s2 N2^a N1) + (N1_{xx}+N1_{yy}) + \alpha N1 - \alpha N1 (N1+N2)/KK
% N2_t = k(s2 N2^a N1 - s1 N1^a N2) + (N2_{xx}+N2_{yy}) + \alpha N2 - \alpha N2 (N1+N2)/KK 
%where nonlinear terms are treated explicitly and epsilon(u_{xx} + u_{yy}) is treated implicitly
%BC:  Periodic
%IC: N1=1.8+sin(2*pi*xx)+0.5*cos(4*pi*yy);
%    N2=2.0+cos(2*pi*xx)+0.5*sin(4*pi*yy);

% Code based on 2D Allen-Cahn Eq using pseudo-spectral with Implicit/Explicit time stepping
% from https://en.wikibooks.org/wiki/Parallel_Spectral_Numerical_Methods/Examples_in_Matlab_and_Python#The_2D_Allen-Cahn_Equation
clear all; clc;

% Parameters
k=10;
a=1.37;
s1=0.45;
s2=1-s1;
alpha=0.03;
KK=0.1;
%Grid
N = 128; h = 1/N; x = h*(1:N);
dt = .0025;


%x and y meshgrid
y=x';
[xx,yy]=meshgrid(x,y);

%initial conditions
N1=1.8+sin(2*pi*xx)+0.5*cos(4*pi*yy);
N2=2+cos(2*pi*xx)+0.5*sin(4*pi*yy);

%Plots each timestep
figure(1); clf; 
subplot(2,1,1); cla; contour(real(N1)); axis([0 N 0 N -1 1],"square"); 
xlabel x; ylabel y; zlabel N1; colorbar;
title(['f1 Time ',num2str(0)]); 
subplot(2,1,2); cla; contour(real(N2)); axis([0 N 0 N -1 1],"square");
xlabel x; ylabel y; zlabel N2; colorbar;
title(['f2 Time ',num2str(0)]); 
drawnow;

%(ik) and (ik)^2 vectors in x and y direction
kx=(2*pi*1i*[0:N/2-1 0 -N/2+1:-1]);
ky=(2*pi*1i*[0:N/2-1 0 -N/2+1:-1]');
k2x=kx.^2;
k2y=ky.^2;

[kxx,kyy]=meshgrid(k2x,k2y);
        
for n = 1:200
 %calculates nonlinear terms in real space
 N1_nl=k*(s1*(N1.^a).*N2 - s2*(N2.^a).*N1) - alpha*N1.*(N1+N2)/KK; 
 N2_nl=k*(s2*(N2.^a).*N1 - s1*(N1.^a).*N2) - alpha*N2.*(N1+N2)/KK; 
 
 %FFT for linear and nonlinear term
 N1_nl = fft2(N1_nl);
 N1_hat=fft2(N1);
 N2_nl = fft2(N2_nl);
 N2_hat=fft2(N2);
 N1new=(N1_hat*(alpha + 1/dt) + N1_nl)./ ...
       (-(kxx+kyy) + 1/dt); %Implicit/Explicit timestepping
 N2new=(N2_hat*(alpha + 1/dt) + N2_nl)./ ...
       (-(kxx+kyy) + 1/dt); %Implicit/Explicit timestepping
 %converts to real space in x-direction
 N1=real(ifft2(N1new));
 N2=real(ifft2(N2new));
 %Plots each timestep
 t=n*dt;
 figure(1); clf; 
 subplot(2,1,1); cla; contour(real(N1)); axis([0 N 0 N -1 1],"square");
 xlabel x; ylabel y; zlabel f1; colorbar;
 title(['N1 Time ',num2str(t)]); 
 subplot(2,1,2); cla; contour(real(N2)); axis([0 N 0 N -1 1],"square");
 xlabel x; ylabel y; zlabel f2; colorbar;
 title(['N2 Time ',num2str(t)]); 
 drawnow;
end
