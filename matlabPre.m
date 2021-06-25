function mls = matlabPre(path)
arcRess = [];
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
% normalMe = abs(normalMe);
[s, f, t, p] = spectrogram(normalMe,h,wlen-hop,yxis,333e3);
for o = 1:(length(normalMe)/hop) 
    PF = 0;
    for r = 5:240 
        PF = PF+p(r, o)/r;
    end
    res(o) = PF;
end
flag = 0;
for o = 1:(length(normalMe)/hop)
    if res(o) > 2e-5
        flag = flag+1;
    end
end
arcRess = [arcRess res*10e7];
mls = arcRess';
end