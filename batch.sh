# For Section 3
for data in flickr delicious twitter_tag_out_going
do
  python outdegree_distribution.py ${data} > result.${data}.outdegree
  python indegree_distribution.py ${data} > result.${data}.indegree
  python multiplicity.py ${data} > result.${data}.multiplicity
  python behaviors.py ${data} > result.${data}.behaviors
done

# For Section 4
tagging_data=twitter_tagging
following_data=twitter_following
python in_out.py ${tagging_data} > result.in_out
python rp_at_m.py ${tagging_data} > result.rp_at_m
python rp_at_t.py ${tagging_data} > result.rp_at_t
python tag_follow_disagreement.py ${tagging_data} ${following_data} > result.disagreement
python forward_mutual.py ${tagging_data} ${following_data} > result.forward_mutual
