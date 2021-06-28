function t= demo(path)
arcRess = [];% ????????
arcFeature = [];

normalDataO=load(path);
normalData= normalDataO.y;
normalData=normalData(:, 2);
normalMe = normalData(2*333e4:30*333e4);
% Z-Score???
normalAvg = mean(normalMe);
[m, n] = size(normalMe);
normalVariation = sqrt(sum((normalMe - normalAvg).*(normalMe - normalAvg)) / m);
normalRange = normalMe - normalAvg;
normalMe = normalRange / normalVariation;
% normalS = (normalMe - min(normalMe)) / (max(normalMe) - min(normalMe));
% ????
temp = sqrt((abs(normalMe) - normalAvg).*(abs(normalMe) - normalAvg)/ m);
v = max(temp)-min(temp);
ss = mean(temp);
for i = 2:size(temp)
    distance = normalMe(i)-normalMe(i-1);
    if abs(temp(i)-ss)/v >0.02 && abs(distance) > 0.05
        normalMe(i) = normalMe(i-1);
    end
end
wlen=512;%???????????????????????????
hop=333e1;%???????????1??????????????????
h=hamming(wlen);%????????
yxis = 1000;
% normalMe = abs(normalMe);
[s, f, t, p] = spectrogram(normalMe,h,wlen-hop,yxis,333e3);
for o = 1:(length(normalMe)/hop) % ?hop????????????/hop
    PF = 0;
    for r = 5:240 % ???1.5KHz-80KHz??????????
        PF = PF+p(r, o)/r;
    end
    res(o) = PF;
end
flag = [];
for r = 1:40:200 % ?????????????????
    flag = [flag, p(r, :)'*10e7];
end
for r = 1:5
    for col = 1:28000
        if flag(col, r) > 20
            r_feature(col, r) = 1;
        else
            r_feature(col, r) = 0;
        end
    end
end

arcRess = [arcRess res*10e7];
arcFeature = [arcFeature; r_feature];

xlswrite("E:/arcDetection/data.xlsx",arcRess')
xlswrite("E:/arcDetection/feature.xlsx",arcFeature)
t= 1;
end