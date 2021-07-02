function mls = matlabPre(path)
normalDataO=load(path);
normalData= normalDataO.y;
normalData=normalData(:, 2);
normalMe = normalData(2*333e4:30*333e4);
normalAvg = mean(normalMe);
[m, n] = size(normalMe);
normalVariation = sqrt(sum((normalMe - normalAvg).*(normalMe - normalAvg)) / m);
normalRange = normalMe - normalAvg;
normalMe = normalRange / normalVariation;
temp = sqrt((abs(normalMe) - normalAvg).*(abs(normalMe) - normalAvg)/ m);
v = max(temp)-min(temp);
ss = mean(temp);
for i = 2:size(temp)
    distance = normalMe(i)-normalMe(i-1);
    if abs(temp(i)-ss)/v >0.02 && abs(distance) > 0.05
        normalMe(i) = normalMe(i-1);
    end
end
wlen=512;
hop=333e1;
h=hamming(wlen);
yxis = 1000;
[s, f, t, p] = spectrogram(normalMe,h,wlen-hop,yxis,333e3);
for o = 1:(length(normalMe)/hop) % ?hop????????????/hop
        PF = 0;
        for r = 5:240 % ???1.5KHz-80KHz??????????
            PF = PF+p(r, o)/r;
        end
       res(o) = PF;
end

arcRess =res*10e7;
arcFeatureHigh = abs(real(s(10,:)));
arcFeatureLow = abs(real(s(2,:)));

mls = [arcRess',arcFeatureLow',arcFeatureHigh'];
end