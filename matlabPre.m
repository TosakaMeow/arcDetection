function mls = matlabPre(path)
normalDataO=load(path);
normalData= normalDataO.normalData;
normalMe = normalData(2*333e4:30*333e4);
normalAvg = mean(normalMe);
[m, n] = size(normalMe);
normalVariation = sqrt(sum((normalMe - normalAvg).*(normalMe - normalAvg)) / m);
normalRange = normalMe - normalAvg;
normalMe = normalRange / normalVariation;
wlen=512;
hop=333e1;
h=hamming(wlen);
yxis = 1000;
[s, f, t, p] = spectrogram(normalMe,h,wlen-hop,yxis,333e3);
for o = 1:(length(normalMe)/hop)
        tmp = normalMe(3330*(o-1)+1:3330*(o));
        res(o) = sum(abs(tmp));
end
res = (res - min(res))/(max(res)-min(res));
AL = abs(real(s(5,:)));
AL = (AL - min(AL))/(max(AL)-min(AL));
AH = abs(real(s(13,:)));
AH = (AH - min(AH))/(max(AH)-min(AH));
arcRess =res;
arcFeatureHigh = AH;
arcFeatureLow = AL;

mls = [arcRess'*5, arcFeatureLow'*5, arcFeatureHigh'*5];
end