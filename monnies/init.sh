if [ ! "$@" ]; then
    pip install tweepy
else
    for monnie in "$@"
    do
        case $monnie in
        twitter)
            pip install tweepy
            ;;
        *)
            echo "Unrecognized monnie:" $monnie
            ;;
        esac
    done
fi



