#Simple firestore update

from google.cloud import firestore

def increment(request):
    incr_by = request.args.get('incr_by', 1)
    
    db = firestore.Client()

    site_visit_ref = db.collection(u'cloud-resume-site').document(u'doc-site-visits')
    site_visit_ref.update({'visits': firestore.Increment(incr_by)})
    site_visit_get = site_visit_ref.get()
    site_visit_dict = site_visit_get.to_dict()

    return site_visit_dict

