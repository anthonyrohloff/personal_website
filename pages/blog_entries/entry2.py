import dash
from dash import html, dcc

dash.register_page(__name__, path="/blog/entry2", title="How I Passed Security+ without any Experience")

post_content = """
# How I Passed Security+ without any Experience

As a new college student aspiring to become a cybersecurity professional, I found myself wondering how I could learn about the field. After scouring the web to determine the best way to go about this endeavor, I determined that I would go for Security+. However, I had never done anything like this before, and it was a nerve-wracking thought to put so much time, effort, and money into something and potentially get nothing in return. I knew I was capable of it, but I needed to build up my confidence.

This is when I decided to take on SC-900, Microsoft Certified: Security, Compliance, and Identity Fundamentals. It seemed like it covered some similar topics but had much less overall content. This, combined with the much lower price tag ($381 for Security+ and $99 for SC-900), made it an attractive option. According to the information I could find on it, it is a super-beginner certification helping people get their feet wet in some areas and feel out the certification-earning process.

There was one issue. Finals were quickly approaching. I had a little over a month until the semester ended. Thus, I gave myself one month to earn the certificate, start-to-finish. I pored over the content Microsoft provides for free on their website and tried to figure out a method of taking notes that worked for me. I started with written notes, but my handwriting is far too messy for those to be useful. I moved on to flash cards and decided to stick with them since they were quick to make and easy to practice.

The weeks went by. I was focused on my classes, SC-900, and my job. This busy schedule showed me how much work I can take on if I plan my time effectively. I finished the Microsoft content in about three weeks and focused on review for the last week. It was hard to find balance at times, but in the end, the test was scheduled and I passed with ease. That was what I needed to see. Passing this test removed my imposter syndrome and gave me confidence to take the next step, Security+.

I waited until the semester was over to embark on this next adventure. I was heading down to BMW Manufacturing Co. in South Carolina to start my first rotation as a Controls Engineer Co-op. This was an exciting opportunity for me for many reasons, the most relevant one being that I would have no distractions. No friends, family, or girlfriend to take my attention away from studying for Security+, and on top of that, a consistent daily schedule to help keep my routine strong. 

I began studying immediately, giving myself the length of the 16-week rotation to earn the certification. I knew I likely would not need that much time, but I wanted to be sure I was ready. There is no free content for Security+ like there was for SC-900, so I went searching for a way to learn. I landed on Dion Training’s Security+ SY0-701 course on Udemy. It provided about 35 hours of content that I knew I would need for the exam. I set out to do an hour per day so I wouldn’t get burned out. However, I was trying to take thorough notes and make flash cards for everything so I would have all the information I needed, which proved to be an impossible task at the level of detail I was going into. One hour of videos per day turned into two or more hours of total study time. This was not feasible as I still had a full-time job. I decided to eliminate written notes again and only took flash cards that I thought were important. This routine set in, and I kept going even when it was challenging. I was staring at a screen working my brain for 8 hours at work every day, and then I would come home and do it for another hour or two more. Studying for these certifications has instilled a work ethic in me that I didn’t know I had. 

After about 8 weeks, I finished the course. It took me that long because I didn’t just watch videos every day. Some days I would go through flash cards or try to learn more about a topic that confused me. I was trying to make sure I fully understood each concept before moving on to avoid having to go back. I took about two more weeks to review and go through some practice tests I bought. Finally, I scheduled the exam.

The day of the exam was a rollercoaster of emotions. It was Saturday, so I did not work. I woke up early and made sure to eat a good breakfast and get myself in the right mindset. I told myself there was nothing else to do now but take the test so worrying is pointless. Before the test began, I went through a few topics that I was struggling with to ease my nerves. Then, it was time for the exam.

It felt extremely disheartening to see questions I had no idea how to answer, but I felt that there were quite a few more that I knew without question. I was on the fence through the entire multiple-choice section, wondering “Am I passing? Am I failing?” Pressing forward, I went on to the performance-based questions, which were supposedly heavily weighted in scoring. I took a deep breath and started to tackle them. To my delight, they went down quickly and easily. I checked my answers and submitted my exam. Once I found out I passed I threw my arms up in joy and exhaustion. 

This had been a difficult challenge, but I knew I was so much better because of it. I had learned many technical concepts, but the most important takeaway was learning what I was capable of. Since then, I have built many projects that I would be too scared to attempt previously, and I have plans to go for another certification soon. This time, it will be in the realm of penetration testing. I can’t wait to start diving back into the certification game with this experience behind me.
"""

layout = html.Div([
    dcc.Markdown(post_content, style={'padding': '20px', 'font-size': '18px'}),
])
