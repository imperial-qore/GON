for model in 'GON' 'USAD' 'MAD_GAN' 'SlimGAN' 'DILOF' 'IF' 'TranAD' 'ONLAD'; do
	for dataset in 'SMD' 'MSDS' 'FTSAD-1' 'FTSAD-25' 'FTSAD-55'; do
		python3 main.py --model $model --dataset $dataset --retrain --notest
	done
done