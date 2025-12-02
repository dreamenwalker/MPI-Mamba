function C  = PhanFunc( Xn, Yn, figName2 )

im2 = imread(figName2);
if size(im2,3)>1
    im2 = rgb2gray(im2);
end
C=imresize(im2,[Xn,Yn],'nearest');

[x,y]=size(C);
C=im2double(C);
for i=1:1:x
    for j=1:1:y
         C(i,j)=C(i,j)/256;
         %         if C(i,j)>125
%             C(i,j)=1;
%         else
%             C(i,j)=0;
%         end
    end
end

end