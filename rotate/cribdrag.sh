# Usage:
for i in {0..26}; do
    wait
    python cribdragging.py "${i}" >> out.log
    echo "----" >> out.log
done;